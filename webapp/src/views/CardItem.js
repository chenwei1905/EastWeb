import { Layout, Menu, Card } from "antd";
import React, { useState } from "react";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined
} from "@ant-design/icons";

const CardItem = props => {
    const {title, content}  = props;
    return (
        <div>
            <Card title={title} style={{ width: 300 }}>
                <p>{content}</p>
            </Card>
        </div>
    );
};
