// Load here global React objects like a navbar, i18n flags clicks, etc...
// We can load our Sass stylesheets which will be included in the bundle using Webpack,
// thus we can also setup JavaScript things ... all of those will be used everywhere in our app

import { checkStatus, getCSRFToken, getCurrentLang } from 'Utils'

// Load the CSS stylesheets for our dependencies
require('../css/bootstrap.min.css')
require('../css/animate.min.css')
require('../css/toastr.min.css')

// Load our base Sass stylesheet
require('../scss/style.scss')

// Setup momentjs to be french :)
moment.locale('fr')

// Setup raven (Sentry client)
Raven.config('http://02c622eee5004e9fa9b661395e6ca409@localhost:8081/3').install()


const Flag = React.createClass({

    handleClick() {
        console.log(getCurrentLang())
        var data = {language: this.props.lang,
                    next: '/',
                    csrfmiddlewaretoken: getCSRFToken()}

        fetch('/i18n/setlang/',
        {
            body: JSON.stringify(data),
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        })
        .then(checkStatus)
        .then(response => {
            // refresh page + flush i18n cookie ?
            console.log(data)
            console.log(getCurrentLang())
            console.log('isok')
            // top.location.reload()
        })
        .catch(err => {
            // Error during request, or parsing NOK :(
            console.log('/i18n/setlang/' + this.props.lang, err)
        })
    },

    render() {
        return (
            <li>
                <a className={"lang-select " + this.props.lang}
                   onClick={this.handleClick}>
                    <img className={"lang-select-flag-" + this.props.lang}
                         alt={this.props.langname}
                         src={"/static/img/" + this.props.lang + ".gif"}
                         />
                </a>
            </li>
        )
    }
})

class Flags extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <ul className="nav navbar-nav pull-right">
                <Flag lang="eu" langname="Euskara"/>
                <Flag lang="fr" langname="Français"/>
            </ul>
        )
    }
}

ReactDOM.render(
    <Flags />,
    document.getElementById('flags')
)