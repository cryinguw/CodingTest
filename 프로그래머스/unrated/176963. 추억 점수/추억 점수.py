def make_yearning_dict(name, yearning):
    new_yearning_dict = {}
    for name_value, yearning_value in zip(name, yearning):
        new_yearning_dict[name_value] = yearning_value
        
    return new_yearning_dict


def solution(name, yearning, photo):
    answer = []
    
    yearning_dict = make_yearning_dict(
        name=name, yearning=yearning
    )
    
    for picture in photo:
        score = 0
        
        for name in picture:
            if name in yearning_dict:
                score += yearning_dict[name]
        answer.append(score)
    
    return answer