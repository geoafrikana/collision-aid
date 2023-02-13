const formData = new FormData();

// let dummyForm = {}
let form = document.getElementById('rate-survey-form')

let arr = ['Sample Biz',
 '10, Glover Street, Lagos Island, Lagos, Nigeria',
'+2349037838682', 'Lagos','http://www.geoafrikana.com',
 'Nasiru', 'Olagunju','Principal Consultant', '234-555-1234',
 'nasir@geoafrikana.com','nasir@geoafrikana.com',
 20, 50, 70, 100, 200, 50,60, 50, 39, 200,
250, 175, 110, 89, 91, 180, 42, 5, 67, 29]

let formFields = document.getElementsByClassName('f')
formFields = [...formFields]
let idArr = []
let valArr = []

formFields.map((item, idx)=>{
        item.value = arr[idx]
        if(item.id != 'confirm_email'){
            idArr.push(item.id)
            valArr.push(item.value)
        }
        
})

console.log(idArr)


form.addEventListener('submit', (event)=>{
    event.preventDefault();

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    for (let i=0; i < 30; i++){
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
            console.log('done')
        })
})
