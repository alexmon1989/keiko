const path = require('path');
const webpack = require('webpack');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const TerserPlugin = require('terser-webpack-plugin');

const mode = process.env.NODE_ENV === 'production' ? 'production' : 'development';
module.exports  = {
    mode: mode,
    context: __dirname,
    entry: ['./assets/js/index'],
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: 'app.js'
    },

    optimization: {
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    ecma: undefined,
                    warnings: false,
                    parse: {},
                    compress: {},
                    mangle: true, // Note `mangle.properties` is `false` by default.
                    module: false,
                    output: null,
                    toplevel: false,
                    nameCache: null,
                    ie8: false,
                    keep_classnames: undefined,
                    keep_fnames: false,
                    safari10: false,
                },
            }),
            new OptimizeCSSAssetsPlugin({
                cssProcessor: require("cssnano"),
                cssProcessorPluginOptions: {
                    preset: ["default", {discardComments: {removeAll: true}}]
                }
            })
        ]
    },

    plugins: [
        new VueLoaderPlugin(),
        new webpack.ProvidePlugin({
            jQuery: 'jquery',
            '$': 'jquery',
            'window.jQuery': 'jquery',
        }),
        new MiniCssExtractPlugin({
            filename: "styles.css"
        })
    ],

    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: [
                    'style-loader',
                    MiniCssExtractPlugin.loader,
                    {
                        loader: "css-loader",
                        options: {
                            minimize: true,
                            sourceMap: true
                        }
                    },
                    {
                        loader: "sass-loader"
                    }
                ]
            },
            {
                test: /\.(png|woff|woff2|eot|ttf|svg)$/,
                loader: 'file-loader',
                options: {
                    publicPath: '/static/bundles/'
                }
            }
        ],
    },
    resolve: {
        modules: ['node_modules'],
        alias: {vue: mode === 'production' ? 'vue/dist/vue.min.js' : 'vue/dist/vue.js'}
    },
};