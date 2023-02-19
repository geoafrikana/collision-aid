const contactForm = document.getElementById('contact-form')

const IdFields = ['fname', 'lname', 'email','subject', 'message']

const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value

 const formData = new FormData()

contactForm.addEventListener('submit', (e)=>{
    e.preventDefault();
    for (let i = 0; i< IdFields.length; i++){
       let value = document.getElementById(IdFields[i]).value
       formData.append(IdFields[i], value)
}

    const request = new Request(
        contactForm.action,
        {
            method: 'POST',
            headers: {
                'X-CSRFtoken':
                    csrfToken
            },
            mode: 'same-origin',
            body: formData

        })


            fetch(request)
        .then(res => res.json())
        .then((data) => {
            let {status, message} = data
            let feedback = document.getElementById('feedback')
            feedback.classList.add(`alert-${status}`)
            feedback.innerText = message
            feedback.classList.add(`alert-${status}`)
            feedback.style.setProperty('display', 'block')
            for (let i = 0; i< IdFields.length; i++){
                document.getElementById(IdFields[i]).readOnly = true;
         }
         document.getElementById('submit').disabled =  true
         document.getElementById('submit').style.backgroundColor =  '#808080'
         document.getElementById('submit').style.color = '#fff'
            return
        })


})
