
function Get-PrimeList {
    param(
        [parameter(Mandatory=$true)]
        [int]
        $StartNum, 

        [parameter(Mandatory=$true)]
        [int]
        $EndNum
    )

    #$PrimeList = [System.Collections.ArrayList]@()
    $PrimeList = @()
    foreach ($Number in $StartNum..$EndNum) {
        #Write-Host $("Num: $Number")
        $RunningNum = 2
        $Prime = $true

        if ($Number -lt 2) {
            $Prime = $false
        }

        if ($Number -eq 2) {
            $Prime = $true
        }

        while ($RunningNum -lt $Number) {
            #Write-Host $("Run: $RunningNum")
            if (!($Number % $RunningNum)) {
                $Prime = $false
                break
            }
            $RunningNum++
        }

        if ($Prime) {
            #Write-Host $("Prime: $Number")
            #$PrimeList.Add($Number)
            $PrimeList += $Number

        }
    }
    return $PrimeList
}


Function Get-ArrayDupes {
   param($Array)

   $Hash = @{}
   $Array | %{ $Hash[$_] = $Hash[$_] + 1 }
   $Result = $Hash.GetEnumerator() | ?{$_.value -gt 1} | %{$_.key}

   Return $Result
}


Function Split-Number {
    param(
        [parameter(Mandatory=$true)]
        [int32]
        $Number
    )

    $StrNumber = [string]$Number
    $NumList = @()

    foreach ($Digit in ($StrNumber -Split "")) {
        $Digit
        $NumList += $Digit
    }
}


$PList = Get-PrimeList -StartNum 1000 -EndNum 20000
, $PList

$Num = 55125
$List = Split-Number -Number $Num 
#$List


Get-ArrayDupes -Array $List


