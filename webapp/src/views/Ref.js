import React from "react";

class Child extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            test: "helloXXXXworld",
        }
        this.method = this.method.bind(this);
    };
    method() {
        alert(this.state.test);
    }
    render() {
        return(
            <div>
               <h1>你好，世界</h1>
            </div>
        )
    }
}


class Parent extends React.Component {
    constructor(props) {
        super(props);
        this.click = this.click.bind(this);
    };
    click() {
        this.refs.child.method();
    }
    render() {
        return (
            <div>
                <Child ref="child"/>
                <button onClick={this.click} />
            </div>
        )
    }
}


export default Parent;