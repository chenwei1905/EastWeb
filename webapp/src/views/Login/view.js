import React, { useState } from "react";
import { Checkbox, Button, Form, Input } from "antd";
import Icon from '@ant-design/icons';
import { connect } from "react-redux";
import { actions as loginActions } from "./index";
import logo from "../../assets/images/logo.svg";
import styles from "./login.css";

const FormItem = Form.Item;

const Login = (props) => {
    let userNameInput = null;
    const [userName, setUserName] = useState("");
    const [password, setPassword] = useState("");

    const emitEmptyUserName = () => {
        userNameInput.focus();
        setUserName("");
    };

    // const gotoLogin = e => {
    //     e.preventDefault();
    //     login({ userName, password });
    // };

    const login = () => {
        //注意加上请求
        console.log(userName);
        alert("hhhh")
        props.history.push("/Home");
    }

    const userNameSuffix = userName ? (
        <Icon type="close-circle" onClick={emitEmptyUserName} />
    ) : null;
    return (
        <>
         
            <div className={styles.content}>
                <Form onSubmit={login} className={styles["login-form"]}>
                    <h3>欢迎登陆</h3>
                    <FormItem>
                        <Input
                            placeholder="用户名: admin Or user"
                            prefix={<Icon type="user" />}
                            suffix={userNameSuffix}
                            value={userName}
                            onChange={e => setUserName(e.target.value)}
                            ref={node => (userNameInput = node)}
                            size="large"
                        />
                    </FormItem>
                    <FormItem>
                        <Input
                            type="password"
                            placeholder="密码: 123456"
                            prefix={<Icon type="eye" />}
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                            size="large"
                        />
                    </FormItem>
                    <FormItem>
                        <Checkbox>记住</Checkbox>
                        <a className={styles["login-form-forgot"]} href="/">
                            忘记密码
                        </a>
                        <Button
                            type="primary"
                            htmlType="submit"
                            className={styles["login-form-button"]}
                            onClick={login}
                        >
                            登陆
                        </Button>
                        <a href ="/">注册</a>
                    </FormItem>
                </Form>
            </div>
            <div className={styles['footer']} >
                版权所有@ XXX有限公司 2020
            </div>
        </>
    );
};

export {Login};