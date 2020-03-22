import { Layout, Dropdown, Button, Menu, Row, Col, Tabs } from "antd";

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


import fileUtil from "./../utils/file/fileUtil";
//引进图表类型配置
import chartsType from "../components/echarts/chartsType.json"
/**
 * 引用对象类型
 */
import Echart1 from "./../components/echarts/echart1";
import Echart2 from "./../components/echarts/echart2";
import Echart3 from "./../components/echarts/echart3";

import View from "./../components/echarts/index"




const { Header, Footer, Sider, Content } = Layout;
const { SubMenu } = Menu;
const { TabPane } = Tabs;




class Home1 extends React.Component {
    constructor(props) {
        super(props);
        this.newTabIndex = 0;
        this.state = {
            tabsData: tabsData,
            activeKey: tabsData[0].key,
        };
        this.onChange = this.onChange.bind(this);
        this.onEdit = this.onEdit.bind(this);
        this.add = this.add.bind(this);
        this.remove = this.remove.bind(this);
        this.handleMenuClick = this.handleMenuClick.bind(this);
      
    }

    onChange = activeKey => {
        this.setState({ activeKey });
    };

    onEdit = (targetKey, action) => {
        this[action](targetKey);
    };

    add = () => {
        const { tabsData } = this.state;
        const activeKey = `newTab${this.newTabIndex++}`;
        tabsData.push({ title: 'New Tab', content: 'New Tab Pane', key: activeKey });
        this.setState({ tabsData, activeKey });
        //fs不允许在浏览器中执行
        //fileUtil(this.state.tabsData, "./../components/layout/content/tabsContent.json").write();
    };

    remove = targetKey => {

        let { activeKey } = this.state;
        let lastIndex;
        this.state.tabsData.forEach((pane, i) => {
            if (pane.key === targetKey) {
                lastIndex = i - 1;
            }
        });
        const tabsData = this.state.tabsData.filter(pane => pane.key !== targetKey);
        if (tabsData.length && activeKey === targetKey) {
            if (lastIndex >= 0) {
                activeKey = tabsData[lastIndex].key;
            } else {
                activeKey = tabsData[0].key;
            }
        }
        this.setState({ tabsData, activeKey });
        //fs模块不能在浏览器中执行
        //fileUtil(this.state.tabsData, "./../components/layout/content/tabsContent.json").write();

    };
    /**
     * 插入表格
     */
    handleMenuClick =(e) =>{
        // message.info('Click on menu item.');
        console.log('click', e);
        console.log(chartsType[e.key].name)
        console.log(chartsType);
        console.log("+++++++被点击的页面是++++++++")
        console.log(this.state.activeKey);
        this.state.tabsData[this.state.activeKey].content = (<View />);
        this.setState({
            tabsData: this.state.tabsData
        })
    
    }
   
    
    

    render() {
        let menu = (
            <Menu onClick={this.handleMenuClick}>
                {chartsType.map((item, index) => (<Menu.Item key={index}>
        
                    <UserOutlined />
                    {item.name}
        
                </Menu.Item>))}
            </Menu>
        );
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
                            <Button icon={<FileOutlined />} onClick={this.add}>打开</Button>
                            <Button icon={<FileAddOutlined />}>增加</Button>
                        </Col>
                        <Col span={12}>
                            {" "}
                            <Dropdown overlay={menu}>
                                <Button icon={<AreaChartOutlined />}>
                                    插入图表
                                </Button>
                            </Dropdown>
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
                                <Tabs

                                    onChange={this.onChange}
                                    activeKey={this.state.activeKey}
                                    type="editable-card"
                                    onEdit={this.onEdit}
                                    onTabClick={() => { }}
                                >
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
