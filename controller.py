import web
from models import RegisterModel,LoginModel,Posts
web.config.debug = False
url=(
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity' , 'PostActivity',
    '/submit-comment', 'SubmitComment',

)
app=web.application(url, globals())
session=web.session.Session(app,web.session.DiskStore("sessions"), initializer={'user':None})#actual,how store
session_data=session._initializer
render=web.template.render("views/template", base="main_layout" ,globals={'session':session_data,'current_user':session_data['user']})

class Home:
    def GET(self):
        # data=type('obj',(object,),{"username":"cycosan11","password":"Guitar121"})
        # login = LoginModel.LoginModel()
        # isCorrect = login.check_user(data)
        # if isCorrect:
        #     session_data["user"] = isCorrect
        post_model=Posts.Posts()
        posts=post_model.get_all_post()
        return render.Home(posts)
class Register:
    def GET(self):
        return render.Register()
class Login:
    def GET(self):
        return render.Login()
class PostRegistration:
    def POST(self):
        data=web.input()
        reg_model=RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username
class CheckLogin:
    def POST(self):
        data=web.input()
        login=LoginModel.LoginModel()
        isCorrect=login.check_user(data)
        if isCorrect:
            session_data["user"]=isCorrect
            return isCorrect


        return "error"
class Logout:
    def GET(self):
        session_data['user']=None
        session['user']=None
        session.kill()
        return "success"
class PostActivity:
    def POST(self):
        data = web.input()

        # We need to store posts with every user's name to tell who posted what
        data.username = session_data['user']['username']

        # Here we will make a call to out model Posts.py inside that we will call Posts class
        post_model = Posts.Posts()
        post_model.insert_post(data)
        return 'success'
class SubmitComment:
    def POST(self):
        data=web.input()
        data.username=session_data["user"]["username"]
        post_model=Posts.Posts()
        added_comment=post_model.add_comment(data)
        if added_comment:
            return added_comment
        else:
            return {"error":"403"}
if __name__=="__main__":
    app.run()
