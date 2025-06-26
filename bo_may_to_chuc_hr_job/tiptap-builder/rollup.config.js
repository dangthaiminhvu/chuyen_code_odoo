import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';

export default [
  {
    input: 'src/index.js',   // chúng ta sẽ tự tạo file này bên dưới
    output: {
      file: '../static/lib/tiptap/tiptap.umd.js',
      format: 'umd',
      name: 'tiptap',        // tên global var khi include <script>
      exports: 'named',
      sourcemap: true,
    },
    plugins: [
      resolve(),
      commonjs(),
      terser(),
    ],
  },
  {
    input: 'src/slash-menu.js',
    output: {
      file: '../static/lib/tiptap/slash-menu.umd.js',
      format: 'umd',
      name: 'SlashMenu',
      exports: 'default',
      sourcemap: true,
    },
    plugins: [
      resolve(),
      commonjs(),
      terser(),
    ],
  }
];
