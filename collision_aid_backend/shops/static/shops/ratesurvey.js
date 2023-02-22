const formData = new FormData();

let form = document.getElementById('rate-survey-form')

const validateEmails =  async()=>{
    email = document.getElementById('email').value
    confirm_email = document.getElementById('confirm_email').value
    if (email != confirm_email) {
     await document.getElementById('email').scrollIntoView()
        alert('Email fields do not match')
        return 'invalid'
    }
   }

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const emailValidation = validateEmails();
    if(emailValidation === 'invalid'){
        return
    }
    else{

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    let formFields = document.getElementsByClassName('f')
    formFields = [...formFields]
    let idArr = []
    let valArr = []

    formFields.map((item) => {
        if (item.id != 'confirm_email') {
            idArr.push(item.id)
            valArr.push(item.value)
        }

    })

    for (let i = 0; i < 30; i++) {
        let key = idArr[i]
        let val = valArr[i]
        formData.append(key, val)
    }

    const request = new Request(
        form.action,
        {
            method: 'POST',
            headers: {
                'X-CSRFtoken':
                    csrftoken
            },
            mode: 'same-origin',
            body: formData
        })

    fetch(request)
        .then(res => res.json())
        .then((data) => {
            alert(data.message)
        })

    }
})
