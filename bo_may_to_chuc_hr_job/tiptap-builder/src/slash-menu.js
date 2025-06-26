import { Extension } from '@tiptap/core';
import Suggestion from '@tiptap/suggestion';

/**
 * SlashMenu: khi gõ '/', hiển thị danh sách lệnh do bạn định nghĩa.
 */
const SlashMenu = Extension.create({
  name: 'slashMenu',

  addOptions() {
    return {
      suggestion: {
        char: '/',
        startOfLine: true,
        /**
         * items({ query }) trả về mảng các item {title, command()}, 
         * filter theo query nếu muốn.
         */
        items: ({ query }) => {
          const all = [
            { title: 'Danh sách có dấu đầu dòng', command: ({ editor, range }) => editor.chain().focus().toggleBulletList().run() },
            { title: 'Danh sách đánh số',        command: ({ editor, range }) => editor.chain().focus().toggleOrderedList().run() },
            { title: 'Bảng',                     command: ({ editor, range }) => editor.chain().focus().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run() },
            { title: 'Dấu phân cách',            command: ({ editor, range }) => editor.chain().focus().setHorizontalRule().run() },
            { title: 'Trích dẫn',                command: ({ editor, range }) => editor.chain().focus().toggleBlockquote().run() },
            { title: 'Mã',                       command: ({ editor, range }) => editor.chain().focus().toggleCodeBlock().run() },
          ];
          if (!query) {
            return all;
          }
          return all.filter(item => item.title.toLowerCase().includes(query.toLowerCase()));
        },
        /**
         * command callback khi chọn 1 item.
         * editor, range, props sẽ được tiptap truyền vào.
         */
        command: ({ editor, range, props }) => {
          props.command({ editor, range, props });
        },
      }
    }
  },

  addProseMirrorPlugins() {
    return [
      Suggestion({
        editor: this.editor,
        ...this.options.suggestion,
      })
    ]
  }
});

export default SlashMenu;
