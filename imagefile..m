inputFile = '/home/r210785/Downloads/IMG_20230724_185435_363.jpg';

imageData = imread(inputFile);
redChannel = imageData(:,:,1);
greenChannel = imageData(:,:,2);
blueChannel = imageData(:,:,3);

redOutputFile = 'a_red_channel.csv';
greenOutputFile = 'a_green_channel.csv';
blueOutputFile = 'a_blue_channel.csv';
csvwrite(redOutputFile, redChannel);
csvwrite(greenOutputFile, greenChannel);
csvwrite(blueOutputFile, blueChannel);

disp('Red, green, and blue channels saved to separate CSV files successfully!');
