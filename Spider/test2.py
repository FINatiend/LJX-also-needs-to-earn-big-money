import re
if __name__ == '__main__':
    str = """
    <li>
            <div class="item">
                <div class="pic">
                    <em class="">2</em>
                    <a href="https://movie.douban.com/subject/1291546/">
                        <img width="100" alt="霸王别姬" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2561716440.jpg" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1291546/" class="">
                            <span class="title">霸王别姬</span>
                                <span class="other">&nbsp;/&nbsp;再见，我的妾  /  Farewell My Concubine</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 陈凯歌 Kaige Chen&nbsp;&nbsp;&nbsp;主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...<br>
                            1993&nbsp;/&nbsp;中国大陆 中国香港&nbsp;/&nbsp;剧情 爱情 同性
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.6</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1477907人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">风华绝代。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">3</em>
                    <a href="https://movie.douban.com/subject/1292720/">
                        <img width="100" alt="阿甘正传" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1484728154.jpg" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292720/" class="">
                            <span class="title">阿甘正传</span>
                                    <span class="title">&nbsp;/&nbsp;Forrest Gump</span>
                                <span class="other">&nbsp;/&nbsp;福雷斯特·冈普</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 罗伯特·泽米吉斯 Robert Zemeckis&nbsp;&nbsp;&nbsp;主演: 汤姆·汉克斯 Tom Hanks / ...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;剧情 爱情
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.5</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1512416人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">一部美国近现代史。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        
    """
    pattern = re.compile('<li>.*?em class="">(\d+)</em>.*?title">(.*?)</span>.*?title">.*?class="">(.*?)<br>'
                         + '(.*?)</p>.*?average">(.*?)</span>.*?content.*?</div>.*?</li>', re.S)
    print(re.findall(pattern,str))