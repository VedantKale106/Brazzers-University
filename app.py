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
            'position': 'Director of Plumbing Department',
            'image': '/static/images/johnny.jpg'
        },
        {
            'name': 'Dr. Sunny Leone',
            'position': 'Academic Coordinator',
            'image': '/static/images/sunny.jpg'
        },
        {
            'name': 'Dr. Jordi El Nino',
            'position': 'Student Representative',
            'image': '/static/images/jordy.jpg'
        },
        {
            'name': 'Prof. Sudipa',
            'position': 'Head of Desi Department',
            'image': '/static/images/sudipa.webp'
        },
        {
            'name': 'Dr. Lana Rhoades',
            'position': 'Dean of Stepfantasy Foundation',
            'image': '/static/images/lana.jpg'
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



