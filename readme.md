pip install flask-sqlalchemy
pip install flask-migrate

flask db init
flask db migrate -m "user table"
flask db upgrade  create the table
flask db downgrade  undo the change

flask db history
flask db current


delete data:

users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
db.session.commit()

posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
>>> db.session.commit()
db.session.commit()

password hash
from werkzeug.security import generate_password_hash, check_password_hash
hash = gererate_password_hash('testing')
check_password_hash(hash, 'testing')
return true

u = User(username='Echo', email='echo@demo.com')
>>> u.set_password('testing')
>>> u.check_password('password')
False
>>> u.check_password('testing')

pip install flask-login

UserMixin

database many to many

user1  = User.query.get(1)
user2 = User.query.get(2)

>>> user1.is_following(user2)
False
>>> user1.follow(user2)
>>> user1.is_following(user2)
True

user1.is_following(user2)  return flase or true
user1.follow(user2)
user1.unfollow(user2)
user1.followed.all()  user1 is following which users
user1.followers.all()  user1's followers



Page 1, implicit: http://localhost:5000/index
Page 1, explicit: http://localhost:5000/index?page=1
Page 3: http://localhost:5000/index?page=3

http://127.0.0.1:5000/explore?page=2

paginate: 显示第一页的内容， 每页显示三个post
posts = Post.query.order_by(Post.timestamp.desc()).paginate(1, 3, False).items

has_next: 是否还有下一页
has_prev: 是否还有上一页
items: 返回当前页的所有内容
next(error_out=False): 返回下一页的Pagination对象
prev(error_out=False): 返回上一页的Pagination对象
page: 当前页的页码（从1开始）
pages: 总页数
per_page: 每页显示的数量
perv_num: 上一页页码数
next_num: 下一页页码数
query: 返回 创建这个Pagination对象的查询对象
total: 查询返回的记录总数
iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2)


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)  默认显示第一页的内容
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    如果有下一页， page设为下一页页码数  explore?page=2
    next_url = url_for('explore', page=posts.next_num) if posts.has_next else None
    如果有上一页， page设为上一页页码数  explore?page=1
    prev_url = url_for('explore', page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html', title='Explore', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


email support

pip install flask-email
pip install pyjwt   # JSON Web Tokens

token  = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256')
>>> token
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjoiYiJ9.dvOo58OBDHiuSHD4uW88nfJikhYAXc_sfUHq1mDi4G0'
>>> jwt.decode(token, 'my-secret', algorithm=['HS256'])
{'a': 'b'}

facelift

pip install flask-bootstrap

dates and times

pip install flask-moment

moment('2017-09-28T21:45:23Z').format('L')
"09/28/2017"
moment('2017-09-28T21:45:23Z').format('LL')
"September 28, 2017"
moment('2017-09-28T21:45:23Z').format('LLL')
"September 28, 2017 2:45 PM"
moment('2017-09-28T21:45:23Z').format('LLLL')
"Thursday, September 28, 2017 2:45 PM"
moment('2017-09-28T21:45:23Z').format('dddd')
"Thursday"
moment('2017-09-28T21:45:23Z').fromNow()
"7 hours ago"
moment('2017-09-28T21:45:23Z').calendar()
"Today at 2:45 PM"



