from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional, Regexp
from flask_login import current_user
from models import User

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    submit = SubmitField('Đăng nhập')

class RegistrationForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired(), Length(min=4, max=80)])
    name = StringField('Họ và tên', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Xác nhận mật khẩu', 
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Đăng ký')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Tên đăng nhập đã tồn tại')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email đã được đăng ký')

class UserForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[
        DataRequired(message="Vui lòng nhập tên đăng nhập"),
        Length(min=4, max=80, message="Tên đăng nhập phải từ 4-80 ký tự"),
        Regexp(r'^[\w.@+-]+$', message="Tên đăng nhập chỉ được chứa chữ cái, số và các ký tự . @ + -")
    ])
    name = StringField('Họ và tên', validators=[
        DataRequired(message="Vui lòng nhập họ tên"),
        Length(max=100, message="Họ tên không được quá 100 ký tự")
    ])
    email = EmailField('Email', validators=[
        DataRequired(message="Vui lòng nhập email"),
        Email(message="Email không hợp lệ")
    ])
    password = PasswordField('Mật khẩu', validators=[
        DataRequired(message="Vui lòng nhập mật khẩu"),
        Length(min=6, message="Mật khẩu phải có ít nhất 6 ký tự")
    ])
    role_id = SelectField('Vai trò', coerce=int, validators=[
        DataRequired(message="Vui lòng chọn vai trò")
    ])
    submit = SubmitField('Lưu')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user and (not current_user or user.id != current_user.id):
            raise ValidationError('Tên đăng nhập đã tồn tại')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user and (not current_user or user.id != current_user.id):
            raise ValidationError('Email đã được đăng ký')

class UserPermissionForm(FlaskForm):
    role = SelectField('Vai trò', coerce=int)
    permissions = SelectMultipleField('Quyền hạn', choices=[
        ('view_users', 'Xem danh sách người dùng'),
        ('edit_users', 'Chỉnh sửa người dùng'),
        ('delete_users', 'Xóa người dùng'),
        ('manage_roles', 'Quản lý vai trò')
    ])
    submit = SubmitField('Cập nhật')