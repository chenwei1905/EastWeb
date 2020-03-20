var fs = require(fs);

export default fileUtil = (jsonData,filePath) => {

    write = (jsonData, filePath) => {
        let jsonResult = JSON.stringify(jsonData, "", "\t");

        fs.writeFile(filePath, jsonResult, (err) => {
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