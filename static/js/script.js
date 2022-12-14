let pass1 = document.querySelector('#password1')
let pass2 = document.querySelector('#password2')

let submit = document.querySelector('#submit')
let message = document.querySelector('#message')

pass1.addEventListener('input', e => {
    if(pass1.value.length < 8){
        message.innerHTML = `
            <div class="alert alert-danger">Пароль должен состоять минимум из 8 символов</div>
        ` 
        submit.setAttribute('disabled', '')
    }else {
        message.innerHTML = ''     
    }
})

pass2.addEventListener('input', e => {
    if (pass1.value !== pass2.value){
        message.innerHTML = `
            <div class="alert alert-danger">Пароли не совпадают</div>
        `
        submit.setAttribute('disabled', '')
    } else if (pass1.value === pass2.value  && pass2.value !== '') {
        submit.removeAttribute('disabled')
        message.innerHTML = ''
    }
})
