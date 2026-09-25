// parser.js — parsea logs IWC de Samsung (Q-learning WiFi)

const RE_TS         = /^\[(\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]/;
const RE_GOOD       = /Good Link.*RSSI:(-?\d+).*AP:(##:##:##:##:[0-9a-f:]+)/;
const RE_POOR       = /Poor Link.*RSSI:(-?\d+)\s+AP:(##:##:##:##:[0-9a-f:]+)/;
const RE_CONN       = /Connecting event.*new AP:(##:##:##:##:[0-9a-f:]+)/;
const RE_DISCONN    = /Auto Disconnection.*RSSI=(-?\d+).*Old AP=(##:##:##:##:[0-9a-f:]+)/;
const RE_FOREGROUND = /Foreground package,:\s+(\S+)/;
const RE_QTAB       = /Qtable Dump: < (##:##:##:##:[0-9a-f:]+) - ([\d.]+) ([\d.]+) ([\d.]+) >/;
const RE_QTAB_ACT   = /Q-Table: \[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+);.*Action Taken: (\d+)/;
const RE_NET_DISC   = /Network disconnected event.*RSSI=(-?\d+)/;

function parseLine(line) {
  const tsMatch = line.match(RE_TS);
  if (!tsMatch) return null;
  const ts = tsMatch[1];
  const rest = line.slice(tsMatch[0].length);

  let m;
  if ((m = rest.match(RE_GOOD)))
    return { ts, type: 'good_link', rssi: +m[1], bssid: m[2] };
  if ((m = rest.match(RE_POOR)))
    return { ts, type: 'poor_link', rssi: +m[1], bssid: m[2] };
  if ((m = rest.match(RE_CONN)))
    return { ts, type: 'connect', bssid: m[1] };
  if ((m = rest.match(RE_DISCONN)))
    return { ts, type: 'disconnect', rssi: +m[1], bssid: m[2] };
  if ((m = rest.match(RE_NET_DISC)))
    return { ts, type: 'net_disconnect', rssi: +m[1] };
  if ((m = rest.match(RE_FOREGROUND)))
    return { ts, type: 'app', app: m[1] };
  if ((m = rest.match(RE_QTAB)))
    return { ts, type: 'qtable', bssid: m[1], q0: +m[2], q1: +m[3], q2: +m[4] };
  if ((m = rest.match(RE_QTAB_ACT)))
    return { ts, type: 'qaction', q0: +m[1], q1: +m[2], q2: +m[3], action: +m[4] };
  return null;
}

function parseLog(text) {
  const events = [];
  for (const line of text.split('\n')) {
    const ev = parseLine(line);
    if (ev) events.push(ev);
  }
  return events;
}

function summarize(events) {
  const byBssid = {}, byType = {}, byApp = {}, byHour = {};

  for (const e of events) {
    byType[e.type] = (byType[e.type] || 0) + 1;
    if (e.ts && e.ts.length >= 8) {
      const hour = e.ts.slice(6, 8);
      byHour[hour] = (byHour[hour] || 0) + 1;
    }
    if (e.bssid) {
      if (!byBssid[e.bssid]) {
        byBssid[e.bssid] = { count: 0, rssiSum: 0, rssiN: 0,
                             min: 0, max: -200, good: 0, poor: 0 };
      }
      const b = byBssid[e.bssid];
      b.count++;
      if (e.type === 'good_link') b.good++;
      if (e.type === 'poor_link') b.poor++;
      if (typeof e.rssi === 'number') {
        b.rssiSum += e.rssi;
        b.rssiN++;
        if (e.rssi < b.min) b.min = e.rssi;
        if (e.rssi > b.max) b.max = e.rssi;
      }
    }
    if (e.app) byApp[e.app] = (byApp[e.app] || 0) + 1;
  }

  const ranking = Object.entries(byBssid)
    .map(([bssid, d]) => ({
      bssid, count: d.count,
      avgRssi: d.rssiN ? +(d.rssiSum / d.rssiN).toFixed(1) : null,
      min: d.min, max: d.max, good: d.good, poor: d.poor
    }))
    .sort((a, b) => (b.avgRssi ?? -999) - (a.avgRssi ?? -999));

  const apps = Object.entries(byApp)
    .map(([app, n]) => ({ app, n }))
    .sort((a, b) => b.n - a.n);

  const hours = Array.from({ length: 24 }, (_, i) => {
    const k = String(i).padStart(2, '0');
    return { hour: k, n: byHour[k] || 0 };
  });

  return { total: events.length, byType, ranking, apps, hours };
}

window.IWC = { parseLog, summarize };