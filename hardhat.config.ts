import "@shardlabs/starknet-hardhat-plugin";
/**
 * @type import('hardhat/config').HardhatUserConfig
 */

module.exports = {
  cairo: {
    venv: "active",
  },
  networks: {
    local: {
      url: "http://localhost:5000",
    },
  },
};
