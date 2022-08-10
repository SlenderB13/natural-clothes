CEP_API_BASE_URL = 'https://viacep.com.br/ws'

// get postal code
code = ''
$('#postal-code-input').keyup((e) => {
    code = $('#postal-code-input').val()
    return code
})

// use postal code to fetch with viaCep API
$('#search-code-btn').click((e) => {
    e.preventDefault()
    const request = fetch_address(code)
    .then((response) => {
        set_address(response.logradouro)
    })
})

// get all inputs and validate each of them
$('#finish-btn').click(() => {
    $('input[type="text"]').each((index, input) => {
        validate_input(input)
    })
})

const fetch_address = async (code) => {
    const request = await $.ajax({
        url: `${CEP_API_BASE_URL}/${code}/json`,
        dataType: 'json',
        success: (result) => {
            return result
        }
    })
    return request
}

const set_address = (address) => {
    $('#address-street-input').val(`${address}`)
}

const validate_input = (input) => {
    if($(input).val() == '') {
        return $(input).addClass('is-invalid')
    } 

    if($(input).val() != '' && $(input).hasClass('is-invalid')) {
        $(input).removeClass('is-invalid')
        return $(input).addClass('is-valid')
    } 

    return $(input).addClass('is-valid')
}