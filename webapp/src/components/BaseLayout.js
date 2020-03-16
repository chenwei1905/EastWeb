import React from "react";
import { Layout, Menu, Breadcrumb } from "antd";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined
} from "@ant-design/icons";

import "../App.css";

import { HashRouter as Router, Link, Route, withRouter } from "react-router-dom";

const { Header, Content, Footer } = Layout;

class BaseLayout extends React.Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick = e => {
        console.log("click ", e.key);
        console.log(this.props);
        if (e.key == 1) {
            this.props.history.push("/echarts/InventoryManage");
        } 

        if (e.key == 2) {
            this.props.history.push("/echarts/Svg");
        } 
        if (e.key == 3) {
            this.props.history.push("/echarts/EchartsRadar");
        } 

        if (e.key == 4) {
            this.props.history.push("/echarts/Dynamic");
        } 

       
    };
    render() {
        return (
            <Layout className="layout" >
                <Header>
                    <Menu
                        theme="dark"
                        mode="horizontal"
                        defaultSelectedKeys={[this.props.selectKey]}
                        style={{ lineHeight: "64px" }}
                        onClick={this.handleClick}
                    >
                        <Menu.Item key="1">库存管理分析</Menu.Item>
                        <Menu.Item key="2">
                           Svg
                        </Menu.Item>
                        <Menu.Item key="3">
                            EchartsRadar
                        </Menu.Item>
                        <Menu.Item key="4">
                            Dynamic
                        </Menu.Item>
                    </Menu>
                </Header>
                <Content style={{ padding: "0 50px" }}>
                    {/* <Breadcrumb style={{ margin: "16px 0" }}>
                        <Breadcrumb.Item>Home</Breadcrumb.Item>
                        <Breadcrumb.Item>List</Breadcrumb.Item>
                        <Breadcrumb.Item>App</Breadcrumb.Item>
                    </Breadcrumb> */}
                    <div className="site-layout-content">
                        {this.props.children}
                    </div>
                </Content>
                <Footer style={{ textAlign: "center" }}>
                    Ant Design ©2018 Created by Ant UED
                </Footer>
            </Layout>
        );
    }
}
export default withRouter(BaseLayout);
