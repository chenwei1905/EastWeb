import { Layout, Button, Menu, Row, Col, Tabs } from "antd";

import React from "react";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
    GithubOutlined,
    SearchOutlined,
    FileAddOutlined,
    FileOutlined,
    AreaChartOutlined,
    EditOutlined
} from "@ant-design/icons";
import tabsData from "./../components/layout/content/tabsContent.json";

const { Header, Footer, Sider, Content } = Layout;
const { SubMenu } = Menu;
const { TabPane } = Tabs;

class Home1 extends React.Component {
    constructor(props) {
        super(props);
        this.callback = this.callback.bind(this);
        this.state = {
          tabsData: tabsData
        }
    }

    callback(key) {
        console.log(key);
    }

    render() {
        return (
            <Layout>
                <Layout
                    style={{
                        paddingTop: 10,
                        marginBottom: 10
                    }}
                >
                    <Row align="middle" justify="center">
                        <Col span={4}>
                            <GithubOutlined
                                style={{
                                    color: "red",
                                    fontSize: "1.5em",
                                    marginRight: 20
                                }}
                            />{" "}
                            Hello world
                        </Col>
                        <Col span={4}>
                            <Button icon={<FileOutlined />}>打开</Button>
                            <Button icon={<FileAddOutlined />}>增加</Button>
                        </Col>
                        <Col span={12}>
                            {" "}
                            <Button icon={<AreaChartOutlined />}>
                                插入图表
                            </Button>
                        </Col>{" "}
                        <Col span={4}>
                            <Button icon={<EditOutlined />}></Button>
                        </Col>
                    </Row>
                </Layout>
                <Layout>
                    <Content
                        className="site-layout-background"
                        style={{
                            minHeight: 580,
                            backgroundColor: "#FFF"
                        }}
                    >
                        <Row align="middle" justify="left">
                            <Col span={20}>
                                <Tabs onChange={this.callback} type="card">
                                    {this.state.tabsData.map(pane => (
                                        <TabPane
                                            tab={pane.title}
                                            key={pane.key}
                                        >
                                            {pane.content}
                                        </TabPane>
                                    ))}
                                </Tabs>
                            </Col>
                            <Col span={4}></Col>
                        </Row>
                    </Content>
                </Layout>

                <Footer style={{ textAlign: "center", Height: 40 }}>
                    Footer
                </Footer>
            </Layout>
        );
    }
}

export default Home1;
