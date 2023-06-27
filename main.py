
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'L', 'R', 'T']
score = 0
 
@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    print(score)
    request.get_data()
    #logger.info(request.json)
    
    sres=request.json["arena"]["state"]["https://cloud-run-hackathon-python-kt5uau5seq-uc.a.run.app"]
    print(sres)
    if sres["wasHit"]:
        logger.info("hit")
        print("hit")
        #excape from sides
        if sres["x"] == 0 and sres["direction"] != "E":
            logger.info("trun")
            return moves[1] #trun left
        if sres["x"] == 6 and sres["direction"] != "W":
            logger.info("trun")
            return moves[1] #trun left
        if sres["y"] == 0 and sres["direction"] != "S":
            logger.info("trun")
            return moves[1] #trun left
        if sres["y"] == 9 and sres["direction"] != "N":
            logger.info("trun")
            return moves[1] #trun left

        logger.info("move")
        return moves[0]
    else:
        logger.info("miss")
        print("miss")
        print(sres["score"])
        if sres["x"] == 0 and sres["direction"] != "W":
            logger.info("trun")
            return moves[1] #trun left
        if sres["x"] == 6 and sres["direction"] != "E":
            logger.info("trun")
            return moves[1] #trun left
        if sres["y"] == 0 and sres["direction"] != "N":
            logger.info("trun")
            return moves[1] #trun left
        if sres["y"] == 9 and sres["direction"] != "S":
            logger.info("trun")
            return moves[1] #trun left

    if random.choice([True,False]):
        logger.info("move")
        return moves[random.randrange(3)]
    else:
        logger.info("Throw")
        return moves[3]
    
    
    # TODO add your implementation here to replace the random response
    
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
