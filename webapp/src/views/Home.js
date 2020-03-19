import { Layout, Menu } from "antd";
import React, { useState } from "react";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined
} from "@ant-design/icons";

import { view as MySidebar } from "./../components/sidebar";
import data from "./../components/sidebar/data";

const { Header, Sider, Content } = Layout;

const Home = props => {
    return (
        <Layout>
            <MySidebar  urldata={data} />
        </Layout>
    );
};

export default Home;
