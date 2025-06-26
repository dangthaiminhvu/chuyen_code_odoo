/** @odoo-module **/
import { registry } from '@web/core/registry';
import { FieldText } from '@web/views/fields/field_text/field_text';
const { Editor } = window.tiptap;                  // từ lib tiptap.umd.js
const StarterKit = window.StarterKit;               // basic nodes & marks
const SlashMenu = window.SlashMenu.default;         // extension

/**
 * FieldSlashText: mở rộng FieldText, khởi tạo Tiptap với SlashMenu.
 */
class FieldSlashText extends FieldText {
    /**
     * Thiết lập editor ngay khi widget dựng.
     */
    mounted() {
        super.mounted();
        this._initEditor();
    }

    willUnmount() {
        this.editor.destroy();
        super.willUnmount();
    }

    _initEditor() {
        const target = this.el.querySelector('textarea') || this.el;
        this.editor = new Editor({
            element: target,
            extensions: [
                StarterKit,
                SlashMenu.configure({
                    suggestion: {
                        char: '/',
                        startOfLine: true,
                        items: ({ query }) => {
                            const list = [
                                { title: 'Danh sách có dấu đầu dòng', command: () => this.editor.chain().focus().toggleBulletList().run() },
                                { title: 'Danh sách đánh số',        command: () => this.editor.chain().focus().toggleOrderedList().run() },
                                { title: 'Bảng',                     command: () => this.editor.chain().focus().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run() },
                                { title: 'Dấu phân cách',            command: () => this.editor.chain().focus().setHorizontalRule().run() },
                                { title: 'Trích dẫn',                command: () => this.editor.chain().focus().toggleBlockquote().run() },
                                { title: 'Mã',                       command: () => this.editor.chain().focus().toggleCodeBlock().run() },
                            ];
                            if (!query) {
                                return list;
                            }
                            return list.filter(item =>
                                item.title.toLowerCase().includes(query.toLowerCase())
                            );
                        }
                    }
                }),
            ],
            content: this.value || '',
            onUpdate: ({ editor }) => {
                this._setValue(editor.getHTML(), { fromUser: true });
            },
        });
    }
}

// Đăng ký widget mới với tên "slash_text"
registry.category('fields').add('slash_text', FieldSlashText);
