import fs from 'fs'

const fileUtil = (jsonData,filePath) => {

    const write = (jsonData, filePath) => {
        let jsonResult = JSON.stringify(jsonData, "", "\t");

        fs.writeFile(filePath, jsonResult, function(err)  {
            if(err) {
                console.log(err);
            } else {
                console.log("***********保存成功***********");
            }
        })
    }

    return {
        write: write,
    }
   
}

export default fileUtil;