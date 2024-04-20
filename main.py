import streamlit as st
from utils import generate_script

st.title("🎦视频脚本生成器(基于Chatgpt-3.5turbo)")

with st.sidebar:
    openai_api_key = st.text_input("请输入你的OPENAI API密钥：",type="password")
    st.markdown("[获取openai api密钥](https://platform.openai.com/account/api-keys)")
    st.write("可添加我的微信：13152588835。获取API密钥")

subject = st.text_input("请输入视频主题")
video_length = st.number_input("⏳请输入视频大致时长(单位：分钟)",min_value=0.1,step=0.1)
creativity = st.slider("✨请输入视频脚本的创造力(数值越小月严谨，数值越大更多样)",
                       min_value=0.0,max_value=1.0,value=0.2,step=0.1)

submit = st.button("生成脚本")

if submit and not openai_api_key:
    st.info("请输入API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not video_length < 60:
    st.info("咋滴，你要拍电影啊？搞辣么长的视频😡时长调短一点")
if submit and not video_length >= 0.1:
    st.info("视频时长需要大于等于0.1")
    st.stop()


if submit:
    with st.spinner("正在生成，请稍等..."):
        search_result,title,script = generate_script(subject,video_length,creativity,openai_api_key)
    st.success("视频脚本已生成！")
    st.subheader("标题:")
    st.write(title)
    st.subheader("脚本:")
    st.write(script)
    with st.expander("维基百科搜索结果:"):
        st.info(search_result)