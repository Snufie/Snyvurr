import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import { nodePolyfills } from 'vite-plugin-node-polyfills'
import Vue from '@vitejs/plugin-vue'
import VueMacros from 'unplugin-vue-macros'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VueMacros({
      plugins: {
        vue: Vue()
      }
    }),
    nodePolyfills({
      globals: {
        Buffer: true, // can also be 'build', 'dev', or false
        global: true,
        process: true
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src/main.ts', import.meta.url))
    }
  }
})
