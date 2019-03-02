import React from "react"
import ReactDOM from "react-dom"
import WelcomePage from "./WelcomePage"

const App = () => (
  <WelcomePage endpoint="api/map/" />
);

ReactDOM.render(
  <App />,
  document.getElementById("app")
)