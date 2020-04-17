from wtforms import Form, StringField, FloatField, IntegerField, DateTimeField
from wtforms.validators import Length, EqualTo, InputRequired, NumberRange

from models import User


class RegistForm(Form):
    username = StringField(validators=[Length(3, 20)])
    password = StringField(validators=[Length(3, 20)])
    password_repeat = StringField(validators=[EqualTo('password')])


class LoginForm(Form):
    username = StringField(validators=[Length(3, 20)])
    password = StringField(validators=[Length(3, 20)])

    # def validate(self):
    #     result = super(LoginForm, self).validate()
    #     if not result:
    #         return False
    #     username = self.username.data
    #     password = self.password.data
    #     users = User.query.filter(User.username == username,
    #                              User.password == password)
    #     if not users:
    #         self.username.errors.append('用户不存在或密码错误')
    #         return False
    #     return True


class MessageForm(Form):
    kernel_use = IntegerField(validators=[InputRequired(message='不能为空'), NumberRange(1)])
    memory_use = FloatField(validators=[InputRequired(message='不能为空'), NumberRange(0)])
    time_begin = DateTimeField()
    time_end = DateTimeField()
    comment = StringField(validators=[Length(0, 200)])


