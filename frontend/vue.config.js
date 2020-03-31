const webpack = require('webpack')

module.exports = {

  assetsDir: "static",
  configureWebpack: {

    plugins: [

      new webpack.ProvidePlugin({

        $: "jquery",

        jQuery: "jquery",

        jquery: "jquery",

        "windows.jQuery": "jquery"

      })
    ]
  },
}