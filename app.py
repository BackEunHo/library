from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 데이터를 저장할 딕셔너리 초기화
library_data = {
    'members': {},
    'books': {}
}

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html', members=library_data['members'], books=library_data['books'])

# 멤버 추가
@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['member_name']
    phone = request.form['phone_number']
    library_data['members'][name] = phone
    return redirect('/')

# 멤버 삭제
@app.route('/delete_member', methods=['POST'])
def delete_member():
    name = request.form['member_name']
    if name in library_data['members']:
        del library_data['members'][name]
    return redirect('/')

# 책 추가
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['book_title']
    library_data['books'][title] = '대출 가능'
    return redirect('/')

# 책 삭제
@app.route('/delete_book', methods=['POST'])
def delete_book():
    title = request.form['book_title']
    if title in library_data['books']:
        del library_data['books'][title]
    return redirect('/')

# 책 대출
@app.route('/loan_book', methods=['POST'])
def loan_book():
    member_name = request.form['loan_member']
    book_title = request.form['loan_book_title']
    
    if book_title in library_data['books'] and library_data['books'][book_title] == '대출 가능':
        library_data['books'][book_title] = member_name
    return redirect('/')

# 책 반납
@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form['return_member']
    book_title = request.form['return_book_title']
    
    if book_title in library_data['books'] and library_data['books'][book_title] == member_name:
        library_data['books'][book_title] = '대출 가능'
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
