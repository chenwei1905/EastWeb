import { Layout, Menu} from "antd";
import Icon from '@ant-design/icons';
import React, { useState } from "react";
import { Link } from 'react-router-dom';
import './sidebar.css'
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined
} from "@ant-design/icons";
const { SubMenu } = Menu;

const { Header, Sider, Content } = Layout;

const mySidebar = props => {
    const { urldata} = props;
   // const [collapsed, setCollapsed] = useState(false);

    

    return (
        <Sider trigger={null} collapsible collapsed={'true'} >
            <div className="logo" />
            <Menu theme="dark" mode="inline" defaultSelectedKeys={["1"]} >
                {urldata.map(item => {
                    if (item.children instanceof Array) {
                        return (
                            <SubMenu
                                key={item.key}
                                title={
                                    <span>
                                        <Icon type={item.icon} />
                                        <span>{item.label}</span>
                                    </span>
                                }
                            >
                                {item.children.map(subItem => (
                                    <Menu.Item key={subItem.key}>
                                        <Link to={subItem.url}>
                                            {subItem.label}
                                        </Link>
                                    </Menu.Item>
                                ))}
                            </SubMenu>
                        );
                    } else {
                        return (
                            <Menu.Item key={item.key}>
                                 <span>{item.label}</span>
                                <Link to={item.url}>
                                    <Icon type={item.icon} />
                                </Link>
                            </Menu.Item>
                        );
                    }
                })}
            </Menu>
           
        </Sider>
    );
};

export {mySidebar};
