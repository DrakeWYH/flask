import datetime

from flask import Flask, redirect, render_template, request, url_for, session
from flask import views
from sqlalchemy import desc
from models import User, Message
from forms import LoginForm, RegistForm, MessageForm
from exts import db
import config
from auth import login_required

app = Flask(__name__)
app.config.from_object(config)
app.debug = True
db.init_app(app)


class IndexView(views.MethodView):
    def get(self):
        messages = Message.query.filter(Message.time_end > datetime.datetime.now())
        if 'user_id' in session:
            user = User.query.get(session['user_id'])
            return render_template('index.html', user=user, messages=messages)
        return render_template('index.html', messages=messages)


class RegistView(views.MethodView):
    def get(self):
        form = RegistForm()
        return render_template('regist.html', form=form)

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter(User.username == username).first()
            if user:
                form.username.errors.append('该用户已注册！')
                return render_template('regist.html', form=form)
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('regist.html', form=form)


class LoginView(views.MethodView):
    def get(self):
        form = LoginForm()
        return render_template('login.html', form=form)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter(User.username == username, User.password == password).first()
            if not user:
                form.username.errors.append('该用户不存在或密码错误！')
                return render_template('login.html', form=form)
            session['user_id'] = user.id
            return redirect(url_for('index'))
        return render_template('login.html', form=form)


class LogoutView(views.MethodView):
    decorators = [login_required]

    def get(self):
        session.pop(key='user_id')
        return redirect(url_for('index'))


class MessageView(views.MethodView):
    decorators = [login_required]

    def get(self):
        form = MessageForm()
        user = User.query.get(session['user_id'])
        datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return render_template('message.html', user=user, datetime_now=datetime_now, form=form)

    def post(self):
        form = MessageForm(request.form)
        if form.validate():
            user = User.query.get(session['user_id'])
            kernel_use = form.kernel_use.data
            memory_use = form.memory_use.data
            time_begin = form.time_begin.data
            time_end = form.time_end.data
            comment = form.comment.data
            message = Message(
                uid=user.id,
                kernel_use=kernel_use,
                memory_use=memory_use,
                time_begin=time_begin,
                time_end=time_end,
                comment=comment,
            )
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('message'))
        user = User.query.get(session['user_id'])
        datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return render_template('message.html', user=user, datetime_now=datetime_now, form=form)


class MessageStopView(views.MethodView):
    decorator = [login_required]

    def get(self, message_id):
        message = Message.query.get(message_id)
        user = User.query.get(session['user_id'])
        if message and message.uid == user.id:
            message.time_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.commit()
            return redirect(url_for('message'))
        return '信息不存在或无权修改'


class MessageCancelView(views.MethodView):
    decorator = [login_required]

    def get(self, message_id):
        message = Message.query.get(message_id)
        user = User.query.get(session['user_id'])
        if message and message.uid == user.id:
            db.session.delete(message)
            db.session.commit()
            return redirect(url_for('message'))
        return '信息不存在或无权删除'


class AdminView(views.MethodView):
    decorator = [login_required]

    def get(self):
        user = User.query.get(session['user_id'])
        messages = Message.query.order_by(desc('time_end')).all()
        if not user.is_staff:
            return redirect(url_for('index'))
        return render_template('admin.html', user=user, messages=messages)


app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist', view_func=RegistView.as_view('regist'))
app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
app.add_url_rule('/message', view_func=MessageView.as_view('message'))
app.add_url_rule('/message_stop/<int:message_id>', view_func=MessageStopView.as_view('message_stop'))
app.add_url_rule('/message_cancel/<int:message_id>', view_func=MessageCancelView.as_view('message_cancel'))
app.add_url_rule('/admin', view_func=AdminView.as_view('admin'))

# class SendMessageView(views.MethodView):
#     def get(self):
#         return render_template('send_message.html')
#     def post(self):
#         pass


if __name__ == '__main__':
    app.run()
