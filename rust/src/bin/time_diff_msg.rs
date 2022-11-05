/// Problem Statement:
/// You are are given the current time R in the HH:MM:SS format. You are also
/// given N more time values in an array P, where every element P[i] is less than or equal to R.
/// Write a program to calculate the time difference between P[i] and R and print one of the following messages accordingly:
/// > If the time diffeience is zero, print "now".
/// > If the time difference is in seconds but less than a minute, print "X seconds ago".
/// > If the time difference is in minutes but less than an hour, print "X minutes ago". Ignore the seconds pait of the difference.
/// > If the time difference is in hours, print "X hours ago". Ignore the minutes and seconds part of the difference.
/// > if the value of X ts 1, print the word 'second' instead of 'seconds', 'hour' instead of 'hours' and 'minute' instead of 'minutes'.

#[derive(Debug, Clone, PartialEq, Eq)]
struct TimeFormat {
    hour: u64,
    minute: u64,
    second: u64,
}

impl TimeFormat {
    fn from_str(time: &str) -> Result<Self, String> {
        let err_text = "Failed to parse time format!";
        let time: Vec<Result<u64, String>> = time
            .split(':')
            .map(|s| s.parse::<u64>().map_err(|_| err_text.to_string()))
            .collect();
        if time.len() != 3 {
            return Err(err_text.to_string());
        }
        Ok(Self {
            hour: time[0].to_owned()?,
            minute: time[1].to_owned()?,
            second: time[2].to_owned()?,
        })
    }
    fn subtract(&self, time: TimeFormat) -> TimeFormat {
        // this will panic! if `time` is larger ---------\
        let mut diff = self.to_seconds() - time.to_seconds();
        let hours = diff / 3600;
        diff %= 3600;
        let minutes = diff / 60;
        diff %= 60; // seconds left
        Self {
            hour: hours,
            minute: minutes,
            second: diff,
        }
    }
    fn to_seconds(&self) -> u64 {
        self.hour * 3600 + self.minute * 60 + self.second
    }
    fn to_msg(&self) -> String {
        if self.hour == 0 {
            if self.minute == 0 {
                if self.second == 0 {
                    return format!("now");
                } else if self.second == 1 {
                    return format!("{} second ago", self.second);
                }
                return format!("{} seconds ago", self.second);
            } else if self.minute == 1 {
                return format!("{} minute ago", self.minute); // ignoring seconds
            }
            return format!("{} minutes ago", self.minute);
        } else if self.hour == 1 {
            return format!("{} hour ago", self.hour); // ignoring minutes & seconds
        }
        format!("{} hours ago", self.hour)
    }
}

fn main() {
    let curr_time = TimeFormat::from_str("23:34:43").unwrap();
    vec![
        "05:42:21", "00:00:00", "23:34:43", "999:99:9", "23:34:21", "23:12:54",
    ]
    .into_iter()
    .map(|s| TimeFormat::from_str(s).unwrap())
    // filtering off values larger than curr_time - to not panic
    .filter(|time| curr_time.to_seconds() >= time.to_seconds())
    .for_each(|time| println!("{}", curr_time.subtract(time).to_msg()));
}
