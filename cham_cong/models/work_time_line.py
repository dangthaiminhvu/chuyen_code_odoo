from odoo import models, fields

class WorkTimeLine(models.Model):
    _name = 'hr.work.time.line'
    _description = 'Giờ làm việc chi tiết'

    work_time_id = fields.Many2one('hr.work.time', 'Giờ làm việc')
    name = fields.Char('Tên')
    day_of_week = fields.Selection([('0','Chủ nhật'),('1','Thứ hai'),('2','Thứ ba'),('3','Thứ tư'),('4','Thứ năm'),('5','Thứ sáu'),('6','Thứ bảy')], 'Ngày trong tuần')
    time_period = fields.Char('Thời gian trong ngày')
    from_hour = fields.Float('Làm việc từ')
    to_hour = fields.Float('Làm việc đến')
    date_range = fields.Char('Khoảng thời gian')
    work_type = fields.Selection([('normal','Bình thường'),('ot','Làm thêm')], 'Loại công việc')
