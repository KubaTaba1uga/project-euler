fn main(){
    let result = find_fb_numbers(4000000, 0, 1, vec![]);
    println!("result {:?}", result);
}

fn find_fb_numbers(stop_value: u32, value_0: u32, value_1: u32, fb_numbers:Vec<u32>) -> Vec<u32>{
    let mut fb_numbers = fb_numbers;    
    if value_0 < stop_value {
        let result = value_0 + value_1;
        fb_numbers.push(result);
        return find_fb_numbers(stop_value, value_1, result, fb_numbers);
    } else {
        return fb_numbers
    }
}
