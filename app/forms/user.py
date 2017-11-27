from flask_wtf.form import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import User
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.extensions import photos


class RegisterForm(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(), Length(6, 18, message='用户名必须在6~18个字符之间')])
    password = PasswordField('密码',
                             validators=[DataRequired(), Length(6, 18, message='密码长度必须在6~18个字符之间')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致')])
    email = StringField('邮箱', validators=[Email(message='邮箱格式不正确')])
    submit = SubmitField('立即注册')

    # 自定义验证器,验证用户名
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在,请选用其他用户名')

    # 自定义验证器,验证邮箱
    def validate_mail(self, field):
        if User.query.filter_by(mail=field.data).first():
            raise ValidationError('该邮箱已使用,请选用其他邮箱')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密 码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登 陆')



class PasswordForm(FlaskForm):
    old_pwd = PasswordField('原密码', validators=[DataRequired()])
    new_pwd = PasswordField('新密码', validators=[DataRequired(), Length(6, 18, message='密码长度必须在6~18个字符之间')])
    confirm = PasswordField('确认密码', validators=[EqualTo('new_pwd', message='两次密码不一致')])
    submit = SubmitField('确认修改')


class IconForm(FlaskForm):
    icon = FileField('头像', validators=[FileRequired('请选择上传文件'), FileAllowed(photos, '只能上传图片')])
    submit = SubmitField('上传')
