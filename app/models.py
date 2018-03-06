#coding:utf-8
from datetime import datetime
from app import db


#创建会员模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)#编号
    name = db.Column(db.String(100), unique=True)#昵称
    pwd = db.Column(db.String(100))#密码
    email = db.Column(db.String(255), unique=True)#邮箱
    phone = db.Column(db.String(11), unique=True)#手机号
    info = db.Column(db.Text)#简介
    face = db.Column(db.String(255), unique=True)#头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#注册时间
    uuid = db.Column(db.String(255), unique=True)#唯一标识符
    userlogs = db.relationship('Userlog', backref='user')#会员日志外键关系关联
    comments = db.relationship('Comment', backref='user')#电影评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='user')

    def __repr__(self):
        return "<User %r>" % self.name

#会员登录日志模型
class Userlog(db.Model):
    __tablename__='userlog' #表名
    id = db.Column(db.Integer, primary_key=True) #编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #所属会员
    ip = db.Column(db.String(100))#登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now) #登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id

#标签
class Tag(db.Model):
    __tablename__ = 'tag' #表名
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100), unique=True)#昵称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间
    movies = db.relationship('Movie', backref='tag')#电影外键关系关联

    def __repr__(self):
        return "<Tag %r>" % self.name

#电影
class Movie(db.Model):
    __tablename__='movie' #表名
    id = db.Column(db.Integer, primary_key=True)#编号
    title = db.Column(db.String(100), unique=True)#标题
    url = db.Column(db.String(255),unique=True)#地址
    info = db.Column(db.Text)#简介
    logo = db.Column(db.String(255),unique=True)#封面
    star = db.Column(db.SmallInteger)#星级
    playnum = db.Column(db.BigInteger)#播放量
    commentnum = db.Column(db.BigInteger)#评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))#所属标签编号
    ares = db.Column(db.String(255))#上映区域
    release_time = db.Column(db.Date)#上映时间
    length = db.Column(db.String(100))#电影长度
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间
    comments = db.relationship('Comment', backref='movie')#评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='movie')#收藏外键关系关联

    def __repr__(self):
        return "<Movie %r>" % self.title

#上映预告
class Preview(db.Model):
    __tablename__='preview' #表名
    id = db.Column(db.Integer, primary_key=True)#编号
    title = db.Column(db.String(100), unique=True)#标题
    logo = db.Column(db.String(255),unique=True)#封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间

    def ___repr__(self):
        return "<Preview %r>" % self.title

#评论
class Comment(db.Model):
    __tablename__='comment' #表名
    id = db.Column(db.Integer, primary_key=True)#编号
    content = db.Column(db.Text)#内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))#所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间

    def __repr__(self):
        return "<Comment %r>" % self.id

#收藏
class Moviecol(db.Model):
    __tablename__ = 'moviecol'#表名
    id = db.Column(db.Integer, primary_key=True)#编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#所属会员
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))#所属电影
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间

    def __repr__(self):
        return "<Moviecol %r>" % self.id

#权限
class Auth(db.Model):
    __tablename__ = 'auth'#表名
    id = db.Column(db.Integer, primary_key=True)#编号
    name = db.Column(db.String(100), unique=True)#名称
    url = db.Column(db.String(255), unique=True)#地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name

#角色
class Role(db.Model):
    __tablename__ = 'role'#表名
    id = db.Column(db.Integer, primary_key=True)#编号
    name = db.Column(db.String(100), unique=True)#名称
    auths= db.Column(db.String(600))#权限列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#登录时间
    admins = db.relationship("Admin", backref="role")
    def __repr__(self):
        return "<Role %r>" % self.name


#管理员
class Admin(db.Model):
    __tablename__ = 'admin'#表面
    id = db.Column(db.Integer, primary_key=True)#编号
    name = db.Column(db.String(100), unique=True)#管理员账号名称
    pwd = db.Column(db.String(100))#管理员账号密码
    is_super = db.Column(db.SmallInteger)#是否是超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间
    adminlogs = db.relationship("Adminlog", backref="admin")#管理员日志外键关系联结
    oplogs = db.relationship("Oplog", backref="admin")#操作日志外键关系联结

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)

#管理员登陆日志
class Adminlog(db.Model):
    ___table__name = 'adminlog'#表名
    id = db.Column(db.Integer, primary_key=True)#编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))#所属管理员编号
    ip = db.Column(db.String(100))#登录ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)#添加时间

    def __repr__(self):
        return "<Adminlog %r>" % self.id

#操作日志数据模型
class Oplog(db.Model):
    __tablename__ = 'oplog'#表名
    id = db.Column(db.Integer, primary_key=True)#编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))#登录ip
    reason = db.Column(db.String(600))#操作原因
    addtime = db.Column(db.DateTime,index=True,default=datetime.now)#操作时间

    def __repr__(self):
        return "<Oplog %r>" % self.id


#把以上这些模型生成一个数据表 "
#if __name__ == "__main__":
    # db.create_all()
    """
    role = Role(
        name="超级管理员",
        auths=""
    )
    db.session.add(role)
    db.session.commit()
    """
    # from werkzeug.security import generate_password_hash
    # admin = Admin(
    #     name="imoocmovie",
    #     pwd=generate_password_hash("imoocmovie"),
    #     is_super=0,
    #     role_id=1
    # )
    # db.session.add(admin)
    # db.session.commit()

