<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\CrawledData;


class CrawledDataController extends Controller
{
    public function index()
    {
       
        $command = escapeshellcmd('python ..\app\Python\CrawlData.py');
        $output = shell_exec($command);
        $TheCrawledData = CrawledData::all();
        return view('welcome')->with('TheCrawledData', $TheCrawledData);
    }
}
