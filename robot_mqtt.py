apiRouter.post('/test1', function(req, res) {
  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleText: {
            text: "hello I'm Ryan"
          }
        }
      ]
    }
  };
  a = 5;
  res.status(200).send(responseBody);
});

apiRouter.post('/test2', function(req, res) {
  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleText: {
            text: "hello I'm Apeach"
          }
        }
      ]
    }
  };
  b = 5;
  res.status(200).send(responseBody);
});

apiRouter.post('/test3', function(req, res) {
  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleText: {
            text: "hello I'm JJ"
          }
        }
      ]
    }
  };
  c = 5;
  res.status(200).send(responseBody);
});

apiRouter.post('/testcatch', function(req, res) {
  const responseBody = {
    version: "2.0",
    template: {
      outputs: [
        {
          simpleText: {
            text: a.toString() + b.toString() + c.toString()
          }
        }
      ]
    }
  };
  res.status(200).send(responseBody);
});

apiRouter.post('/lastTest', function(req, res) {
  console.log(req.body);
  var responseBody;
  var platforms = new Array();


  var items = new Array();
  var tempButton = {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        };
  var tempMap =
    {
      "title": "GoTo1",
      "description": "출발지를 눌러주세요",
      "buttons": [
        {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        },
        {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        },
        {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        }
      ]
    };
  var caroselcount = 0;
  var lastcount = 0;
  var platformcount = 0;

  if (req.body.action.params.testPara == "godel") {
    responseBody = {
      version: "2.0",
      template: {
        outputs: [
          {
            "basicCard": {
              "title": "보물상자",
              "description": "보물상자 안에는 뭐가 있을까",
              "buttons": [
                {
                  "action": "block",
                  "label": "배송하기",
                  "messageText": "배송하기를 누르셨습니다",
                  "blockId": "5e4d51a88192ac000136c558"
                },
                {
                  "action": "message",
                  "label": "취소하기",
                  "messageText": "취소하기"
                }
              ]
            }
          }
        ]
      },
      data: {
        temp1: "no"
      }
    };
  }else if (req.body.action.params.testPara == "StartPoint") {
  platforms.push("TIP");
  platforms.push("비즈니스센터");
  platforms.push("종합관");
  platforms.push("A동");
  platforms.push("C동");
  platforms.push("E동");
  platforms.push("P동");
  platforms.push("산융관");
  caroselcount = parseInt(platforms.length / 3);
  lastcount = platforms.length % 3;

  for (var i = 0; i < caroselcount; i++) {
    items.push({
      "title": "GoTo1",
      "description": "출발지를 눌러주세요",
      "buttons": [
        {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        },
        {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        },
        {
          "action": "block",
          "label": "열어보기",
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        }
      ]
    });
    items[items.length].buttons[0].label = platforms[i*3];
    items[items.length].buttons[1].label = platforms[i*3+1];
    items[items.length].buttons[2].label = platforms[i*3+2];
  }
  items.push({
      "title": "GoTo1",
      "description": "출발지를 눌러주세요",
      "buttons": [
      ]
    });
  for (var i = 0; i < lastcount; i++) {
    items.buttons.push({
          "action": "block",
          "label": platforms[i+(caroselcount*3)],
          "messageText": "짜잔! 우리가 찾던 보물입니다",
          "blockId": "5e4d54b0b617ea000109330e"
        });
  }
    responseBody = {
      version: "2.0",
      template: {
        outputs: [
          {
            "carousel": {
              "type": "basicCard",
              "items": items
            }
          }
        ]
      },
      data: {
        temp1: "no"
      }
    };
  }else if (req.body.action.params.testPara == "EndPoint") {


    responseBody = {
      version: "2.0",
      template: {
      outputs: [
          {
            simpleText: {
              text: "hello I'm JJ"
            }
          }
        ]
      },
      data: {
        temp1: "no"
      }
    };
  }
  res.status(200).send(responseBody);
});
"""
5e4cbe2ab617ea0001610a58
테스트 출발지 : 5e4d51a88192ac000136c558
테스트 도착지 : 5e4d54b0b617ea000109330e

"""
"""
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "보물상자",
          "description": "보물상자 안에는 뭐가 있을까",
          "buttons": [
            {
              "action": "message",
              "label": "열어보기",
              "messageText": "짜잔! 우리가 찾던 보물입니다"
            },
            {
              "action":  "webLink",
              "label": "구경하기",
              "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
            }
          ]
        }
      }
    ]
  }
}

5e4cbe2ab617ea0001610a58

5e4b8a5292690d00019380e3

var para = req.body.action.clientExtra.hihi + 1
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "GoTo1",
              "description": "보물상자 안에는 뭐가 있을까",
              "buttons": [
                {
                  "action": "block",
                  "label": "열어보기",
                  "messageText": "짜잔! 우리가 찾던 보물입니다",
                  "blockId": "5e4cbe2ab617ea0001610a58"
                },
                {
                  "action": "block",
                  "label": "구경하기",
                  "blockId": "5e4b8a5292690d00019380e3",
                  "extra": para
                }
              ]
            },
            {
              "title": "GoTo2",
              "description": "보물상자 안에는 뭐가 있을까",
              "buttons": [
                {
                  "action": "message",
                  "label": "열어보기",
                  "messageText": "짜잔! 우리가 찾던 보물입니다"
                },
                {
                  "action": "webLink",
                  "label": "구경하기",
                  "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                }
              ]
            },
            {
              "title": "GoTo3",
              "description": "보물상자 안에는 뭐가 있을까",
              "buttons": [
                {
                  "action": "message",
                  "label": "열어보기",
                  "messageText": "짜잔! 우리가 찾던 보물입니다"
                },
                {
                  "action": "webLink",
                  "label": "구경하기",
                  "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
"""
"""
{
  intent: {
    id: '5e4cbe2ab617ea0001610a58',
    name: '테스트 블록 두번째',
    extra: { reason: [Object] }
  },
  userRequest: {
    timezone: 'Asia/Seoul',
    params: { surface: 'Kakaotalk.plusfriend' },
    block: { id: '5e4cbe2ab617ea0001610a58', name: '테스트 블록 두번째' },
    utterance: '테스트',
    lang: 'ko',
    user: {
      id: '5b01902e8a07a114baa0f63a6aef25a254883efc566b918a1d12d5b7a4dcef0b68',
      type: 'botUserKey',
      properties: [Object]
    }
  },
  contexts: [],
  bot: { id: '5e1bbea992690d00019eb340!', name: 'KPU_delivery' },
  action: {
    name: 'RTest',
    clientExtra: null,
    params: { testPara: 'TIP' },
    id: '5e4b88bb92690d00019380d0',
    detailParams: { testPara: [Object] }
  }
}

{
  intent: {
    id: '5e4b8a5292690d00019380e3',
    name: '테스트 블록',
    extra: { reason: [Object] }
  },
  userRequest: {
    timezone: 'Asia/Seoul',
    params: { surface: 'Kakaotalk.plusfriend' },
    block: { id: '5e4b8a5292690d00019380e3', name: '테스트 블록' },
    utterance: '이게?',
    lang: 'ko',
    user: {
      id: '5b01902e8a07a114baa0f63a6aef25a254883efc566b918a1d12d5b7a4dcef0b68',
      type: 'botUserKey',
      properties: [Object]
    }
  },
  contexts: [],
  bot: { id: '5e1bbea992690d00019eb340!', name: 'KPU_delivery' },
  action: {
    name: 'RTest',
    clientExtra: null,
    params: {},
    id: '5e4b88bb92690d00019380d0',
    detailParams: {}
  }
}

{
  intent: {
    id: '5e4b8a5292690d00019380e3',
    name: '테스트 블록',
    extra: { reason: [Object] }
  },
  userRequest: {
    timezone: 'Asia/Seoul',
    params: { surface: 'Kakaotalk.plusfriend' },
    block: { id: '5e4b8a5292690d00019380e3', name: '테스트 블록' },
    utterance: '버튼1',
    lang: 'ko',
    user: {
      id: '5b01902e8a07a114baa0f63a6aef25a254883efc566b918a1d12d5b7a4dcef0b68',
      type: 'botUserKey',
      properties: [Object]
    }
  },
  contexts: [],
  bot: { id: '5e1bbea992690d00019eb340!', name: 'KPU_delivery' },
  action: {
    name: 'RTest',
    clientExtra: null,
    params: {},
    id: '5e4b88bb92690d00019380d0',
    detailParams: {}
  }
}
"""