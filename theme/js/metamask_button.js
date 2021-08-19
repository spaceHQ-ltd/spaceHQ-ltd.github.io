var MY_ADDRESS = 'Enter a wallet number here'
    var tipButton = document.querySelector('.tip-button')

    tipButton.addEventListener('click', function() 
        {
        if (typeof web3 === 'undefined') 
            {
            return renderMessage('<div>You need to install <a href=“https://metmask.io“>MetaMask </a> to use this feature.  <a href=“https://metmask.io“>https://metamask.io</a></div>')
            }

        var user_address = web3.eth.accounts[0]

        web3.eth.sendTransaction(
            {
            to: MY_ADDRESS,
            from: user_address,
            value: web3.toWei('0.01', 'ether'),
            }, 
            function (err, transactionHash) 
                {
                if (err) return renderMessage('There was a problem!: ' + err.message)
                renderMessage('Thanks for the generosity!!')
            })
        })

    function renderMessage (message) 
        {
        var messageEl = document.querySelector('.message')
        messageEl.innerHTML = message
        }
