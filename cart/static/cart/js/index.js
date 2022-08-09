CEP_API_BASE_URL = 'https://viacep.com.br/ws'

// get postal code
$('#postal-code-input').keyup((e) => {
    this.code = $('#postal-code-input').val()
})

// use postal code to fetch with viaCep API
$('#search-code-btn').click((e) => {
    e.preventDefault()
    fetch_address(this.code)
    .then((result) => {
        set_address(result.logradouro)
    })
})

// get all inputs and validate each of them
$('#finish-btn').click(() => {
    $('input[type="text"]').each((index, input) => {
        validate_input(input)
    })
})

async function fetch_address(code) {
    const response = await fetch(`${CEP_API_BASE_URL}/${code}/json`, {
        method: 'GET',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'}
    })
    const result = await response.json() 
    return result
}

function set_address(address) {
    $('#address-street-input').val(`${address}`)
}

function validate_input(input) {
    if($(input).val() == '') {
        $(input).addClass('is-invalid')
    } else {
        $(input).removeClass('is-invalid')
        $(input).addClass('is-valid')
    }
}