module.exports = {
  devServer: {
    allowedHosts: "all",
  },
  webpack: {
    configure: (webpackConfig) => {
      // Ensure proper module resolution
      webpackConfig.resolve.extensions = ['.tsx', '.ts', '.jsx', '.js', '.json'];
      return webpackConfig;
    },
  },
};