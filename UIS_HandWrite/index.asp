<!DOCTYPE html>
<html>
<head>
    <meta charset="big5">
    <style>
        canvas {
            border: 1px solid #e6e6e6;
        }
        .sub {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <input type="radio" name="tool" id="huabi" checked><label for="huabi">�e��</label>
        <input type="radio" name="tool" id="shuazi"><label for="shuazi">��l</label>
        <input type="radio" name="tool" id="penqiang"><label for="penqiang">�Q�j</label>
        <input type="radio" name="tool" id="xiangpi"><label for="xiangpi">���</label>
        <div class="sub">
            <select>
                <option>rect</option>
                <option>circle</option>
            </select>
            <label>�j�p(px)</label><input value = '10' class="size">               
        </div>     
    </div>
    <canvas width = "800" height = "600"></canvas>
    <script src="index.js"></script>
</body>
</html>