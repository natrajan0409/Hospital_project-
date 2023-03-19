from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample patient records stored in a list
patient_records = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return redirect(url_for('home'))
    else:
        return redirect(url_for('index'))

@app.route('/home')
def home():
    return render_template('home.html', patient_records=patient_records)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    phone = request.form['phone']
    age = int(request.form['age'])
    sex = request.form['sex']
    diagnosis = request.form['diagnosis']
    treatment = request.form['treatment']
    next_appointment = request.form['next_appointment']

    patient_records.append({
        'S.no': len(patient_records) + 1,
        'Name': name,
        'Phone': phone,
        'Age': age,
        'Sex': sex,
        'Diagnosis': diagnosis,
        'Treatment': treatment,
        'Next appointment date': next_appointment
    })

    return redirect(url_for('home'))

# @app.route('/update_patient', methods=['POST'])
# def update_patient():
#     update_id = int(request.form['update_id'])
#     updated_patient = {
#         'S.no': update_id,
#         'Name': request.form['update_name'],
#         'Phone': request.form['update_phone'],
#         'Age': int(request.form['update_age']),
#         'Sex': request.form['update_sex'],
#         'Diagnosis': request.form['update_diagnosis'],
#         'Treatment': request.form['update_treatment'],
#         'Next appointment date': request.form['update_next_appointment']
#     }

#     index = next((i for i, patient in enumerate(patient_records) if patient['S.no'] == update_id), None)

    # if index is not None:
    #     patient_records[index] = updated_patient

    # return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
