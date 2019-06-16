module.exports = {
  publicPath: '/',
  outputDir: 'web',
  productionSourceMap: false,
  devServer: {
    proxy: 'http://localhost:5000'
  }
}