// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PVAContract {
    struct Genesis {
        string sha256;
        uint256 timestamp;
        string manifiestoHash;
        bool exists;
    }

    mapping(bytes32 => Genesis) public registries;

    event GenesisRegistered(bytes32 indexed hashRoot, uint256 timestamp);

    function registerGenesis(string memory _sha256, uint256 _timestamp) public {
        bytes32 key = keccak256(abi.encodePacked(_sha256));
        require(!registries[key].exists, "Genesis already registered");
        registries[key] = Genesis(_sha256, _timestamp, "", true);
        emit GenesisRegistered(key, _timestamp);
    }

    function registerManifesto(bytes32 _genesisKey, string memory _manifestHash) public {
        require(registries[_genesisKey].exists, "Genesis not found");
        registries[_genesisKey].manifiestoHash = _manifestHash;
    }

    function getGenesis(bytes32 _genesisKey) public view returns (string memory, uint256, string memory) {
        Genesis memory g = registries[_genesisKey];
        return (g.sha256, g.timestamp, g.manifiestoHash);
    }
}
