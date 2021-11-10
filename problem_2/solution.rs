fn main(){
let result = find_even_number_fb(4000000, 0, 1, 0);
println!("result {}", result)
}

fn find_even_number_fb(stop_value: u32, value_0: u32, value_1: u32, sum:u32) -> u32{
    let mut sum = sum;    
    if value_0 < stop_value {
        let result = value_0 + value_1;
        if result % 2 == 0 {
            sum += result
        }
        return find_even_number_fb(stop_value, value_1, result, sum);
    } else {
        return sum
    }
}