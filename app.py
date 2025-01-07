from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    faculty = [
        {
            'name': 'Dr. Mia Khalifa',
            'position': 'Dean of BDSM',
            'image': '/static/images/mia.jpg'
        },
        {
            'name': 'Prof. Johnny Sins',
            'position': 'Head of Plumbing Engineering',
            'image': '/static/images/johnny.jpg'
        },
        {
            'name': 'Dr. Sunny Leone',
            'position': 'Indian Academic Coordinator',
            'image': '/static/images/sunny.jpg'
        }
    ]
    
    gallery = [
        {'image': '/static/images/campuslife.webp', 'caption': 'Campus Life'},
        {'image': '/static/images/research.jpg', 'caption': 'Research Labs'},
        {'image': '/static/images/library.jpg', 'caption': 'Library'},
        {'image': '/static/images/sports.jpg', 'caption': 'Sports Complex'},
        {'image': '/static/images/students.jpg', 'caption': 'Student Events'},
        {'image': '/static/images/graduation.jpg', 'caption': 'Graduation Day'}
    ]
    
    return render_template('index.html', faculty=faculty, gallery=gallery)

if __name__ == '__main__':
    app.run(debug=True)



